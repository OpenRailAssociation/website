# Agent Instructions

Hugo static site for the OpenRail Association ([openrailassociation.org](https://openrailassociation.org)).

## Build and preview

Submodules must be initialized (`git submodule update --init`). Local dev server:

    hugo server

Also available as mise tasks (`mise run preview`, `mise run build`, `mise run linkcheck`). CI uses mise.

## Repo structure

| Path | Purpose |
|---|---|
| `content/` | Markdown pages and news posts |
| `data/*.yml` | Structured data (members, people, nav, projects, etc.) |
| `themes/openrail/` | Local fork of the Hugo theme (layouts, partials, shortcodes, Sass, JS) |
| `themes/hugomods-images/` | Git submodule — do not modify |
| `themes/hugo-cloak-email/` | Git submodule — do not modify |
| `static/` | Static assets (images, documents, badges, favicons) |
| `config.yaml` | Hugo site configuration |

## Key conventions

Read `CONTRIBUTING.md` for full design rules. The critical ones:

- Use `{{< relurl "path" >}}` for static file links (never hardcoded absolute paths)
- Use `{{< relref "/page" >}}` for internal page links
- Complex HTML goes in shortcodes, not inline in content files
- Data-driven content uses `data/*.yml` + a rendering shortcode
- Conventional commits with optional scope: `news`, `members`, `theme`, `ci`, `deps`

## Themes

`themes/openrail/` is a local fork — edit freely. The other two themes are git submodules tracking upstream; don't modify their contents directly.
