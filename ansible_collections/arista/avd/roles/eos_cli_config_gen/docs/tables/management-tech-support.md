=== "Table"

    | Variable | Type | Required | Default | Value Restrictions | Description |
    | -------- | ---- | -------- | ------- | ------------------ | ----------- |
    | [<samp>management_tech_support</samp>](## "management_tech_support") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;policy_show_tech_support</samp>](## "management_tech_support.policy_show_tech_support") | Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;exclude_commands</samp>](## "management_tech_support.policy_show_tech_support.exclude_commands") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- command</samp>](## "management_tech_support.policy_show_tech_support.exclude_commands.[].command") | String |  |  |  | Command to exclude from tech-support |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;type</samp>](## "management_tech_support.policy_show_tech_support.exclude_commands.[].type") | String |  | `text` | Valid Values:<br>- text<br>- json | The supported values for type are platform dependent. |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;include_commands</samp>](## "management_tech_support.policy_show_tech_support.include_commands") | List, items: Dictionary |  |  |  |  |
    | [<samp>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;- command</samp>](## "management_tech_support.policy_show_tech_support.include_commands.[].command") | String |  |  |  | Command to include in tech-support |

=== "YAML"

    ```yaml
    management_tech_support:
      policy_show_tech_support:
        exclude_commands:
          - command: <str>
            type: <str>
        include_commands:
          - command: <str>
    ```
