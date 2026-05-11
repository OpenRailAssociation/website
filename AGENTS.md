# Agent Instructions

Hugo static site for the OpenRail Association ([openrailassociation.org](https://openrailassociation.org)).

## Build and preview

Tooling is managed via mise. Commands:

- `mise run preview` — local dev server
- `mise run build` — production build to `public/`
- `mise run linkcheck` — build then check broken links with lychee

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

Read `CONVENTIONS.md` for design rules. The critical ones:

- Use `{{</* relurl "path" */>}}` for static file links (never hardcoded absolute paths)
- Use `{{</* relref "/page" */>}}` for internal page links
- Complex HTML goes in shortcodes, not inline in content files
- Data-driven content uses `data/*.yml` + a rendering shortcode
- Conventional commits: `feat(scope): description`

## Themes

`themes/openrail/` is a local fork — edit freely. The other two themes are git submodules tracking upstream; don't modify their contents directly.

## Commit conventions

Conventional commits. Scope is typically the area affected: `content`, `theme`, `data`, `ci`, `static`.
