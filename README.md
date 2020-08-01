## DPLHooks

A very lightweight solution to manage multiple containers in one server,
so that it would be cheaper to run microservices.

The project does not take scaling in consideration.
If have certain service has exceeded its limits, then it has outgrown its role and
should be run on its own server or using some powerful container orchestration services such as Kubernetes.

## Environment Variables

Put these to `.env` as `KEY=1sadsah`, without quotation marks.

```
SECRET_KEY=
DEBUG=
```

## Configuration Files

They are located at `.conf` both in production and development.

See example in `examples/.conf-examples`

### .conf/projects.yaml

Here is syntax reference:

```yaml
version: "1"

projects:
    <project_name>:
      repository: <git_repository>.git
      deploy_token: <a long string> 
      docker_image: <docker_image>  # not supported yet
      hosts:
        - <domain_1>
        - <domain_2>
      docker_compose:
         - <filename_1>:
            # the will be set as environment variables to substitute values in docker-compose
            substitute:
              <VARIABLE_1>: <value_1>
      port: <port_number> # Must be unique.
```

To deploy, do `curl -X POST /deploy/ -d '{"token":"<deploy_token>", "project":"<project_name>"}' -H "Content-Type: application/json"`
