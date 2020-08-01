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

