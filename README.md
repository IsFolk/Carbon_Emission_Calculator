# Carbon emission calculator

This is a group project from the ITRI internship project.

(I have consulted with my supervisor regarding whether it can be included as part of my portfolio.)

## Description
Carbon emissions project demo with Vue and Fastapi on AWS EC2.

- yml, Dockerfile: for Docker setup
- frontend: write with Vue3 & Typescript
- backend: write with Fastapi(Python)



**We all use open-source data.**


## Demo video:

https://youtu.be/N4bZNW1D6_4

[![Everything Is AWESOME](https://i.imgur.com/ACrnM5k.png)](https://www.youtube.com/watch?v=N4bZNW1D6_4-Y "Everything Is AWESOME")
![image](https://github.com/IsFolk/Vuejs_with_Fastapi/assets/61446488/674991d9-62f1-460f-b892-d48dfe947b0a)
![image](https://github.com/IsFolk/Vuejs_with_Fastapi/assets/61446488/da418588-9179-4a6c-8447-044492af3cb8)


## Constructs
### Backend: Fastapi
- Python environment
```
fastapi==0.82.0
joblib==1.1.0
pydantic==1.9.2
starlette==0.19.1
uvicorn==0.13.4
scikit-learn==1.1.2
```
- Dockerfile: set environment, running in port 5000
- src/main.py : router to deal with data
- src/models/*.pkl: put model to test (.pkl file)

### Frontend: Vuejs + TypeScript
- Vue3 with TypeScript
- Dockerfile: set environment, running in port 80



## Command to build docker image
```
docker-compose up -d --build
```
