=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>vxlan_interface</samp>](## "vxlan_interface") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;Vxlan1</samp>](## "vxlan_interface.Vxlan1") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;description</samp>](## "vxlan_interface.Vxlan1.description") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;vxlan</samp>](## "vxlan_interface.Vxlan1.vxlan") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;source_interface</samp>](## "vxlan_interface.Vxlan1.vxlan.source_interface") | String |  |  |  | Source Interface Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;controller_client</samp>](## "vxlan_interface.Vxlan1.vxlan.controller_client") | Dictionary |  |  |  | Client to CVX Controllers |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;enabled</samp>](## "vxlan_interface.Vxlan1.vxlan.controller_client.enabled") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;mlag_source_interface</samp>](## "vxlan_interface.Vxlan1.vxlan.mlag_source_interface") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;udp_port</samp>](## "vxlan_interface.Vxlan1.vxlan.udp_port") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;virtual_router_encapsulation_mac_address</samp>](## "vxlan_interface.Vxlan1.vxlan.virtual_router_encapsulation_mac_address") | String |  |  |  | "mlag-system-id" or ethernet_address (H.H.H)<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;bfd_vtep_evpn</samp>](## "vxlan_interface.Vxlan1.vxlan.bfd_vtep_evpn") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;interval</samp>](## "vxlan_interface.Vxlan1.vxlan.bfd_vtep_evpn.interval") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;min_rx</samp>](## "vxlan_interface.Vxlan1.vxlan.bfd_vtep_evpn.min_rx") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multiplier</samp>](## "vxlan_interface.Vxlan1.vxlan.bfd_vtep_evpn.multiplier") | Integer |  |  | Min: 3<br>Max: 50 |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;prefix_list</samp>](## "vxlan_interface.Vxlan1.vxlan.bfd_vtep_evpn.prefix_list") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;qos</samp>](## "vxlan_interface.Vxlan1.vxlan.qos") | Dictionary |  |  |  | For the Traffic Class to be derived based on the outer DSCP field of the incoming VxLan packet, the core ports must be in "DSCP Trust" mode.<br>!!!Warning, only few hardware types with software version >= 4.26.0 support the below knobs to configure Vxlan DSCP mapping.<br> |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;dscp_propagation_encapsulation</samp>](## "vxlan_interface.Vxlan1.vxlan.qos.dscp_propagation_encapsulation") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;map_dscp_to_traffic_class_decapsulation</samp>](## "vxlan_interface.Vxlan1.vxlan.qos.map_dscp_to_traffic_class_decapsulation") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vlans</samp>](## "vxlan_interface.Vxlan1.vxlan.vlans") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- id</samp>](## "vxlan_interface.Vxlan1.vxlan.vlans.[].id") | Integer | Required, Unique |  |  | VLAN ID |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni</samp>](## "vxlan_interface.Vxlan1.vxlan.vlans.[].vni") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast_group</samp>](## "vxlan_interface.Vxlan1.vxlan.vlans.[].multicast_group") | String |  |  |  | IP Multicast Group Address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flood_vteps</samp>](## "vxlan_interface.Vxlan1.vxlan.vlans.[].flood_vteps") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "vxlan_interface.Vxlan1.vxlan.vlans.[].flood_vteps.[].&lt;str&gt;") | String |  |  |  | Remote VTEP IP Address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vrfs</samp>](## "vxlan_interface.Vxlan1.vxlan.vrfs") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- name</samp>](## "vxlan_interface.Vxlan1.vxlan.vrfs.[].name") | String | Required, Unique |  |  | VRF Name |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;vni</samp>](## "vxlan_interface.Vxlan1.vxlan.vrfs.[].vni") | Integer |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;multicast_group</samp>](## "vxlan_interface.Vxlan1.vxlan.vrfs.[].multicast_group") | String |  |  |  | IP Multicast Group Address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flood_vteps</samp>](## "vxlan_interface.Vxlan1.vxlan.flood_vteps") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "vxlan_interface.Vxlan1.vxlan.flood_vteps.[].&lt;str&gt;") | String |  |  |  | Remote VTEP IP Address |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;flood_vtep_learned_data_plane</samp>](## "vxlan_interface.Vxlan1.vxlan.flood_vtep_learned_data_plane") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;eos_cli</samp>](## "vxlan_interface.Vxlan1.eos_cli") | String |  |  |  | Multiline String with EOS CLI rendered directly on the Vxlan interface in the final EOS configuration. |

=== "YAML"

    ```yaml
    vxlan_interface:
      Vxlan1:
        description: <str>
        vxlan:
          source_interface: <str>
          controller_client:
            enabled: <bool>
          mlag_source_interface: <str>
          udp_port: <int>
          virtual_router_encapsulation_mac_address: <str>
          bfd_vtep_evpn:
            interval: <int>
            min_rx: <int>
            multiplier: <int>
            prefix_list: <str>
          qos:
            dscp_propagation_encapsulation: <bool>
            map_dscp_to_traffic_class_decapsulation: <bool>
          vlans:
            - id: <int>
              vni: <int>
              multicast_group: <str>
              flood_vteps:
                - <str>
          vrfs:
            - name: <str>
              vni: <int>
              multicast_group: <str>
          flood_vteps:
            - <str>
          flood_vtep_learned_data_plane: <bool>
        eos_cli: <str>
    ```
