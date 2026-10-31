# Working in this repository

This repository holds one presentation-manager deck as a throughline graph at `idd/`.

- Run `tl -C idd context` first and follow the brief it prints.
- Change the graph only through `tl` (`new`, `amend`, `link`, `unlink`). Never edit a `<UID>.yml` or `.register.yml`
  by hand. Keep `tl -C idd check` at zero errors.
- Everything an agent writes enters as `origin: ai` and `proposed`. Only a person ratifies.
- Every figure or statement on a slide derives from a claim, and every claim from a source with its `url`,
  `publisher`, `checked` date and `found_via`. Never write a claim you have not read a source for.
- Slide text is a small format, one field a line: `eyebrow:`, `bar:`, `notes:`, and per layout `- Label | Text`
  (cards, rows), `- Figure | Label | Text` (stats), `term:`/`lead:`/`body:`/`label:`/`listlead:` (definition),
  `left:`/`right:` with `- L | ...` and `- R | ...` (compare), `accent:`/`body:` (takeaway). Copy an existing slide.
- Speaker notes are written to be spoken: whole sentences, no lists.
