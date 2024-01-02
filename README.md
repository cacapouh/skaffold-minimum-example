# Skaffoldのミニマムな例

初期化:

```
$ skaffold init
```

デモンストレーション:

```
$ skaffold dev
Generating tags...
 - python-app -> python-app:latest
Some taggers failed. Rerun with -vdebug for errors.
Checking cache...
 - python-app: Found Locally
Tags used in deployment:
 - python-app -> python-app:a5ce045711eb79e86586533e8dff569b94bc0d842cfc30ba7e370f20425ce156
Starting deploy...
 - deployment.apps/python-app created
Waiting for deployments to stabilize...
 - deployment/python-app is ready.
Deployments stabilized in 2.155 seconds
Listing files to watch...
 - python-app
Press Ctrl+C to exit
Watching for changes...
[python-app-container] 1 Hello World
[python-app-container] 2 Hello World
[python-app-container] 3 Hello World
[python-app-container] 4 Hello World
[python-app-container] 5 Hello World
^CCleaning up...
 - deployment.apps "python-app" deleted
```