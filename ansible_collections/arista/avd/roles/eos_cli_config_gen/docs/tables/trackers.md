=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>trackers</samp>](## "trackers") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;- name</samp>](## "trackers.[].name") | String | Required, Unique |  |  | Name of tracker object |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;interface</samp>](## "trackers.[].interface") | String | Required |  |  | Name of tracked interface |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;tracked_property</samp>](## "trackers.[].tracked_property") | String |  | `line-protocol` |  | Property to track |

=== "YAML"

    ```yaml
    trackers:
      - name: <str>
        interface: <str>
        tracked_property: <str>
    ```
