# Contributing

You can send contributions and comments to the [OpenRail Association web site](https://openrailassociation.org) by creating pull requests or opening issues in this repository.

## Build and preview

Clone with submodules:

    git clone --recurse-submodules <repo-url>

If already cloned without submodules:

    git submodule update --init

Run the local dev server:

    hugo server

These commands are also available as mise tasks (`mise run preview`, `mise run build`, `mise run linkcheck`), which pin the Hugo version automatically. CI uses mise.

## Navigation

The top navigation bar is reserved for high-level entry points that serve the majority of visitors:

- **Association** — organizational information (about, structure, people)
- **Open Source** — the open source mission and approach
- **News** — announcements and updates
- **Projects** — the project portfolio
- **Members** — member organizations
- **Contact** — how to reach us

New pages that serve a specific audience (e.g. brand guide, contributor docs) are linked from their parent section, not added to the top nav. The top nav should remain stable and short.

## Linking to static files

Always use the `relurl` shortcode for links to files in `static/`:

```markdown
[Download PDF]({{< relurl "documents/my-file.pdf" >}})
```

Do not use hardcoded absolute paths like `/documents/my-file.pdf`. The site is deployed under subdirectories for PR previews, and absolute paths break there.

In shortcodes, use `urls.RelURL`:

```go-html-template
{{- $src := urls.RelURL (.Get "src") -}}
```

## Internal page links

Use `relref` for links between content pages:

```markdown
[About page]({{< relref "/about" >}})
```

## Content structure

- Complex or repeated HTML belongs in shortcodes (`themes/openrail/layouts/shortcodes/`), not inline in markdown files
- Data-driven content (color palettes, member lists) belongs in `data/*.yml` with a shortcode that renders it
- Data file names should use underscores (Hugo accesses `data/my_file.yml` as `site.Data.my_file`)

## Images

The site uses the `hugomods-images` theme for responsive image processing. For simple inline images in shortcodes, use standard `<img>` tags with `urls.RelURL` for the path.

## Commit conventions

This project uses conventional commits. Scope is optional — use it when it's obvious, omit it when a commit crosses boundaries.

Common scopes: `news`, `members`, `theme`, `ci`, `deps`.
