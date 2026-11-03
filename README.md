# presentation-manager deck template

A deck of its own for [presentation-manager](https://presentation-manager.downloadserver.co.uk), kept as a
[throughline](https://github.com/rhodium-org/throughline) graph. Fork it, change the words, and
presentation-manager builds the deck in your tenant's look every time you push.

The deck here is a working example, *Your first deck*. Its six slides explain how this repository works, and every
statement on them rests on a claim with a source. Replace them with yours.

## Get a deck running

1. **Make your copy.** Press **Use this template** on GitHub and create the repository in your own organisation or
   account. Private is fine.
2. **Install or upgrade throughline** (4.6.2 or later):

   ```bash
   pip install --upgrade "throughline>=4.6.2"
   ```

3. **Change the deck with `tl`**, from the `idd` folder. Never edit the `.yml` files by hand: `tl` keeps every item's
   identifier and links, and checks the graph.

   ```bash
   cd idd
   tl context                       # a brief of the graph and how to work in it
   tl amend SER-0001 --title "My talk" --attr slug=my-talk --attr cover_title="My talk"
   tl amend SLD-0001 --text "..."   # change a slide
   tl new SLD --ground THR-0001 --ground CLM-0001 --attr order=7 --attr layout=cards
   tl check                         # must say: graph is sound
   ```

   Change `assets/mark.png` to your own mark: a square PNG, white on a transparent ground.
4. **Make it live: sign the series.** presentation-manager publishes a series only once its series item is
   ratified by a person. In `idd`, run `tl-ratify -C . --by "Your Name"` and sign `SER-0001`, or sign it at
   `https://table.iddn.uk/#/g/<owner>/<repo>/main/idd?show=now`. Commit and push the signature. Sign it again
   whenever you change the series.
5. **Point presentation-manager at it.** You need to run a tenant, or ask whoever does.
   - If the repository is not in an organisation presentation-manager already reads, give your tenant a GitHub token
     for its organisation or account on **Tenant settings**. A fine-grained token with read access to the
     repository's contents is enough.
   - On **Decks of their own**, add the repository, the branch (`main`), the folder (`idd`) and the edition
     (`ED-0001`).

   The deck appears on the Decks page once it is built. If it cannot be built, Decks of their own says why, naming
   the item.

## How a deck is written down

| Folder | What | Here |
|---|---|---|
| `idd/series` | The series: name, audience, cover, whether decks wait for signatures | `SER-0001` |
| `idd/editions` | The deck: subject, presenter, date, speaker notes | `ED-0001` |
| `idd/threads` | Its sections, in order | `THR-0001`, `THR-0002` |
| `idd/slides` | Its slides: order, layout (`cards`, `rows`, `stats`, `definition`, `compare`, `takeaway`, `screenshot`, `video`), words and notes | `SLD-0001` to `SLD-0006` |
| `idd/claims` | What the slides state; a training deck's claims are `guidance` or `product` | `CLM-0001` to `CLM-0005` |
| `idd/sources` | Where each claim comes from: address, publisher, when checked | `SRC-0001` to `SRC-0003` |
| `idd/interests`, `idd/topics` | What the audience wants to know, and what the deck is about | |

Each slide derives from its thread and the claims it states, and each claim from its sources. The kinds of item and
their attributes are the public
[presentation format standard](https://github.com/rhodium-org/throughline-presentation-standard) v2.2.0, composed in
`idd/throughline.toml`. It declares every attribute presentation-manager reads, so the toml adds nothing and must
not redeclare any of them. [standards.iddn.uk](https://standards.iddn.uk/#/g/rhodium-org/throughline-presentation-standard/v2.2.0)
explains what each kind of item holds, gives a brief to hand your AI, and reviews a repository against the standard.

## Signatures

The series item is always signed by a person before anything is published (step 4). Beyond that, the series says
`approval: none`, so each deck is published as soon as it is pushed, without its slides, claims and sources being
signed: good for a first deck. To have nothing published until a person has read and signed every item a deck shows,
set `approval=person` on `SER-0001`. Then sign with
`tl-ratify` in `idd`, or at `https://table.iddn.uk/#/g/<owner>/<repo>/main/idd?show=now`. presentation-manager
shows a deck waiting for signatures as a draft to its tenant's admins and reviewers.

## The look

The deck has no look of its own. presentation-manager builds it in the brand of the tenant that owns it, and in the
brand of every tenant it is offered to.
