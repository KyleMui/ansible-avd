=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>mcs_client</samp>](## "mcs_client") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;shutdown</samp>](## "mcs_client.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;cvx_secondary</samp>](## "mcs_client.cvx_secondary") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;name</samp>](## "mcs_client.cvx_secondary.name") | String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;shutdown</samp>](## "mcs_client.cvx_secondary.shutdown") | Boolean |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;server_hosts</samp>](## "mcs_client.cvx_secondary.server_hosts") | List, items: String |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- &lt;str&gt;</samp>](## "mcs_client.cvx_secondary.server_hosts.[].&lt;str&gt;") | String |  |  |  | IP or hostname |

=== "YAML"

    ```yaml
    mcs_client:
      shutdown: <bool>
      cvx_secondary:
        name: <str>
        shutdown: <bool>
        server_hosts:
          - <str>
    ```
