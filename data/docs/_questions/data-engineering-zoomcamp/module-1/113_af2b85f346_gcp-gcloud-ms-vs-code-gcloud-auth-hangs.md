---
id: af2b85f346
images:
- description: 'image #1'
  id: image_1
  path: images/data-engineering-zoomcamp/image_df9492cb.png
- description: 'image #2'
  id: image_2
  path: images/data-engineering-zoomcamp/image_6b01ae01.png
- description: 'image #3'
  id: image_3
  path: images/data-engineering-zoomcamp/image_bc858c4b.png
- description: 'image #4'
  id: image_4
  path: images/data-engineering-zoomcamp/image_a231d54c.png
- description: 'image #5'
  id: image_5
  path: images/data-engineering-zoomcamp/image_2f5bf08c.png
question: GCP gcloud + MS VS Code - gcloud auth hangs
sort_order: 113
---

If you are using MS VS Code and running `gcloud` in WSL2, when you first try to login to GCP via the `gcloud` CLI with `gcloud auth application-default login`, you may encounter an issue where a message appears and nothing happens:

<{IMAGE:image_1}>

There might be a prompt asking if you want to open it via a browser. If you click on it, it will open a page with an error message:

<{IMAGE:image_2}>

**Solution:**

- Hover over the long link.
- `Ctrl + Click` the long link.
- Click "Configure Trusted Domains here."
- A popup will appear; pick the first or second entry.

<{IMAGE:image_3}>

<{IMAGE:image_4}>

<{IMAGE:image_5}>

Next time you run `gcloud auth`, the login page should pop up via the default browser without issues.