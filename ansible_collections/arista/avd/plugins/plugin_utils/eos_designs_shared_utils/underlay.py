from __future__ import annotations

from functools import cached_property
from typing import TYPE_CHECKING

from ansible_collections.arista.avd.plugins.plugin_utils.utils import get, get_item

if TYPE_CHECKING:
    from .shared_utils import SharedUtils


class UnderlayMixin:
    """
    Mixin Class providing a subset of SharedUtils
    Class should only be used as Mixin to the SharedUtils class
    Using type-hint on self to get proper type-hints on attributes across all Mixins.
    """

    @cached_property
    def underlay_bgp(self: SharedUtils) -> bool:
        return self.bgp and self.underlay_routing_protocol == "ebgp" and self.underlay_router and self.uplink_type == "p2p"

    @cached_property
    def underlay_mpls(self: SharedUtils) -> bool:
        return (
            self.underlay_routing_protocol in ["isis-sr", "isis-ldp", "isis-sr-ldp", "ospf-ldp"]
            and self.mpls_lsr
            and self.underlay_router
            and self.uplink_type == "p2p"
        )

    @cached_property
    def underlay_ldp(self: SharedUtils) -> bool:
        return self.underlay_routing_protocol in ["isis-ldp", "isis-sr-ldp", "ospf-ldp"] and self.underlay_mpls

    @cached_property
    def underlay_sr(self: SharedUtils) -> bool:
        return self.underlay_routing_protocol in ["isis-sr", "isis-sr-ldp"] and self.underlay_mpls

    @cached_property
    def underlay_ospf(self: SharedUtils) -> bool:
        return self.underlay_routing_protocol in ["ospf", "ospf-ldp"] and self.underlay_router and self.uplink_type == "p2p"

    @cached_property
    def underlay_isis(self: SharedUtils) -> bool:
        return self.underlay_routing_protocol in ["isis", "isis-sr", "isis-ldp", "isis-sr-ldp"] and self.underlay_router and self.uplink_type == "p2p"

    @cached_property
    def underlay_ipv6(self: SharedUtils) -> bool:
        return get(self.hostvars, "underlay_ipv6", default=False) and self.underlay_router

    @cached_property
    def underlay_multicast(self: SharedUtils) -> bool:
        return get(self.hostvars, "underlay_multicast") and self.underlay_router

    @cached_property
    def underlay_multicast_rps(self: SharedUtils) -> list[dict] | None:
        if not self.underlay_multicast:
            return None

        return get(self.hostvars, "underlay_multicast_rps")

    @cached_property
    def underlay_multicast_anycast_rp_mode(self: SharedUtils) -> str:
        return get(self.hostvars, "underlay_multicast_anycast_rp.mode", default="pim")

    @cached_property
    def underlay_multicast_rp_interfaces(self: SharedUtils) -> list[dict] | None:
        if self.underlay_multicast_rps is None:
            return None

        underlay_multicast_rp_interfaces = []
        for rp_entry in self.underlay_multicast_rps:
            if (nodes := get(rp_entry, "nodes")) is None:
                continue

            if (node_entry := get_item(nodes, "name", self.hostname)) is None:
                continue

            underlay_multicast_rp_interfaces.append(
                {
                    "name": f"Loopback{node_entry['loopback_number']}",
                    "description": get(node_entry, "description", default="PIM RP"),
                    "ip_address": f"{rp_entry['rp']}/32",
                }
            )

        if underlay_multicast_rp_interfaces:
            return underlay_multicast_rp_interfaces

        return None

    @cached_property
    def underlay_filter_redistribute_connected(self: SharedUtils) -> bool:
        return get(self.hostvars, "underlay_filter_redistribute_connected", default=True) is True

    @cached_property
    def underlay_rfc5549(self: SharedUtils) -> bool:
        return get(self.hostvars, "underlay_rfc5549") is True

    @cached_property
    def underlay_ospf_process_id(self: SharedUtils) -> int:
        return get(self.hostvars, "underlay_ospf_process_id", default=100)

    @cached_property
    def underlay_ospf_area(self: SharedUtils) -> str:
        return get(self.hostvars, "underlay_ospf_area", default="0.0.0.0")

    @cached_property
    def underlay_filter_peer_as(self: SharedUtils) -> bool:
        return get(self.hostvars, "underlay_filter_peer_as") is True and self.evpn_role not in ["client", "server"]
