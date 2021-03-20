# jellyfin-server

Ansible scripts and related things for setting up a Jellyfin server.

To set it up, run:

    $ ansible-pull -U https://github.com/duckinator/jellyfin-server.git jellyfin.yml

## Self-signed certs when listening on "localhost"

If, when having it listen as `localhost`, you get errors about needing sudo in `systemctl status caddy`,
run this:

```
caddy file-server -domain localhost
```

## License

The code is available as open source under the terms of the [MIT License](https://opensource.org/licenses/MIT).

