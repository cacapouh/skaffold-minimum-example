# Skaffoldのミニマムな例

初期化:

```
$ skaffold init
```

デモンストレーション:

```
$ skaffold dev
Generating tags...
 - python-app -> python-app:966d8e8
Checking cache...
 - python-app: Found. Tagging
Tags used in deployment:
 - python-app -> python-app:a5ce045711eb79e86586533e8dff569b94bc0d842cfc30ba7e370f20425ce156
Starting deploy...
 - deployment.apps/python-app created
Waiting for deployments to stabilize...
 - deployment/python-app is ready.
Deployments stabilized in 1.178 second
Listing files to watch...
 - python-app
Press Ctrl+C to exit
Watching for changes...
[python-app-container] 1 Hello World
[python-app-container] 2 Hello World
[python-app-container] 3 Hello World
[python-app-container] 4 Hello World
[python-app-container] 5 Hello World
[python-app-container] 6 Hello World
[python-app-container] 7 Hello World
[python-app-container] 8 Hello World
[python-app-container] 9 Hello World
[python-app-container] 10 Hello World
Generating tags...
 - python-app -> python-app:966d8e8-dirty
Checking cache...
 - python-app: Not found. Building
Starting build...
Found [minikube] context, using local docker daemon.
Building [python-app]...
Target platforms: [linux/arm64]
#0 building with "default" instance using docker driver

#1 [internal] load .dockerignore
#1 transferring context: 2B done
#1 DONE 0.0s

#2 [internal] load build definition from Dockerfile
#2 transferring dockerfile: 176B done
#2 DONE 0.0s

#3 [auth] library/python:pull token for registry-1.docker.io
#3 DONE 0.0s

#4 [internal] load metadata for docker.io/library/python:3.9-slim
#4 DONE 1.4s

#5 [1/4] FROM docker.io/library/python:3.9-slim@sha256:96be08c44307e781fd9ce8e05b49c969b4cb902ec23594f904739c58da3a09ed
#5 DONE 0.0s

#6 [internal] load build context
#6 transferring context: 259B done
#6 DONE 0.0s

#7 [2/4] RUN mkdir /work
#7 CACHED

#8 [3/4] WORKDIR /work
#8 CACHED

#9 [4/4] COPY main.py /work
#9 DONE 0.0s

#10 exporting to image
#10 exporting layers 0.0s done
#10 writing image sha256:d29f9e70d2ecf63c2ae19123a250889df3eb521c730691ab3257be6a6d3c06ec done
#10 naming to docker.io/library/python-app:966d8e8-dirty done
#10 DONE 0.0s
Build [python-app] succeeded
Tags used in deployment:
 - python-app -> python-app:d29f9e70d2ecf63c2ae19123a250889df3eb521c730691ab3257be6a6d3c06ec
Starting deploy...
 - deployment.apps/python-app configured
Waiting for deployments to stabilize...
 - deployment/python-app is ready.
Deployments stabilized in 2.155 seconds
Watching for changes...
[python-app-container] 17 Hello World
[python-app-container] 3 Hello Skaffold
[python-app-container] 18 Hello World
[python-app-container] 4 Hello Skaffold
[python-app-container] 19 Hello World
[python-app-container] 5 Hello Skaffold
[python-app-container] 20 Hello World
[python-app-container] 6 Hello Skaffold
[python-app-container] 21 Hello World
[python-app-container] 7 Hello Skaffold
[python-app-container] 22 Hello World
[python-app-container] 8 Hello Skaffold
[python-app-container] 23 Hello World
[python-app-container] 9 Hello Skaffold
[python-app-container] 24 Hello World
[python-app-container] 10 Hello Skaffold
[python-app-container] 25 Hello World
[python-app-container] 11 Hello Skaffold
[python-app-container] 26 Hello World
[python-app-container] 12 Hello Skaffold
[python-app-container] 27 Hello World
[python-app-container] 13 Hello Skaffold
[python-app-container] 28 Hello World
[python-app-container] 14 Hello Skaffold
[python-app-container] 29 Hello World
[python-app-container] 15 Hello Skaffold
[python-app-container] 30 Hello World
[python-app-container] 16 Hello Skaffold
[python-app-container] 31 Hello World
[python-app-container] 17 Hello Skaffold
[python-app-container] 32 Hello World
[python-app-container] 18 Hello Skaffold
[python-app-container] 33 Hello World
[python-app-container] 19 Hello Skaffold
[python-app-container] 34 Hello World
[python-app-container] 20 Hello Skaffold
[python-app-container] 35 Hello World
[python-app-container] 21 Hello Skaffold
[python-app-container] 36 Hello World
[python-app-container] 22 Hello Skaffold
[python-app-container] 37 Hello World
[python-app-container] 23 Hello Skaffold
[python-app-container] 38 Hello World
[python-app-container] 24 Hello Skaffold
[python-app-container] 39 Hello World
[python-app-container] 25 Hello Skaffold
[python-app-container] 40 Hello World
[python-app-container] 26 Hello Skaffold
[python-app-container] 41 Hello World
[python-app-container] 27 Hello Skaffold
[python-app-container] 42 Hello World
[python-app-container] 28 Hello Skaffold
[python-app-container] 43 Hello World
[python-app-container] 29 Hello Skaffold
[python-app-container] 44 Hello World
[python-app-container] 30 Hello Skaffold
[python-app-container] 45 Hello World
[python-app-container] 31 Hello Skaffold
[python-app-container] rpc error: code = Unknown desc = Error response from daemon: No such container: bcdb34ee31714a73cdd80cf08655486262c09b79e689aa2a2a253807bcb8c878[python-app-container] 32 Hello Skaffold
[python-app-container] 33 Hello Skaffold
[python-app-container] 34 Hello Skaffold
[python-app-container] 35 Hello Skaffold
[python-app-container] 36 Hello Skaffold
[python-app-container] 37 Hello Skaffold
[python-app-container] 38 Hello Skaffold
[python-app-container] 39 Hello Skaffold
^CCleaning up...
 - deployment.apps "python-app" deleted
```