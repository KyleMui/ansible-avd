# management-api-http

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [Management API HTTP](#management-api-http)
- [ACL](#acl)
  - [Standard Access-lists](#standard-access-lists)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | oob_management | oob | MGMT | 10.73.255.122/24 | 10.73.255.2 |

##### IPv6

| Management Interface | description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | oob_management | oob | MGMT | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description oob_management
   vrf MGMT
   ip address 10.73.255.122/24
```

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | True |

Management HTTPS is using the SSL profile SSL_PROFILE

#### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| default | ACL-API | - |
| MGMT | ACL-API | - |

#### Management API HTTP Configuration

```eos
!
management api http-commands
   protocol https
   protocol https ssl profile SSL_PROFILE
   no protocol http
   default-services
   no shutdown
   !
   vrf default
      no shutdown
      ip access-group ACL-API
   !
   vrf MGMT
      no shutdown
      ip access-group ACL-API
```

## ACL

### Standard Access-lists

#### Standard Access-lists Summary

##### ACL-API

| Sequence | Action |
| -------- | ------ |
| 10 | permit 10.0.0.0/8 |
| 20 | permit 100.0.0.0/8 |

#### Standard Access-lists Device Configuration

```eos
!
ip access-list standard ACL-API
   10 permit 10.0.0.0/8
   20 permit 100.0.0.0/8
```
