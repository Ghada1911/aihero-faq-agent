---
id: 0b20afa7bb
question: Deploying to Digital Ocean
sort_order: 28
---

You may quickly deploy your project to DigitalOcean App Cloud. The process is relatively straightforward. The deployment costs about 5 USD/month. The container needs to be up until the end of the project evaluation.

Steps:

1. Register in DigitalOcean.
2. Go to Apps -> Create App.
3. Choose GitHub as a service provider.
4. Edit Source Directory (if your project is not in the repo root).
5. **IMPORTANT**: Go to settings -> App Spec and edit the Dockerfile path so it looks like `./project/Dockerfile` path relative to your repo root.
6. Remember to add model files if they are not built automatically during the container build process.