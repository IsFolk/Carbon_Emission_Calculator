# Vuejs_with_Fastapi

ITRI carbon emissions project demo with Vue and Fastapi.

- yml, Dockerfile: for Docker setup
- frontend: write with Vue3 & Typescript
- backend: write with Fastapi(Python)

If you wanna see the demo site:


[![Watch the video](https://img.youtube.com/vi/N4bZNW1D6_4/default.jpg)](https://youtu.be/N4bZNW1D6_4)


<a href="http://www.youtube.com/watch?feature=player_embedded&v=N4bZNW1D6_4" target="_blank">
 <img src="http://img.youtube.com/vi/N4bZNW1D6_4/mqdefault.jpg" alt="Watch the video" width="240" height="180" border="10" />
</a>

 <iframe width="560" height="315"
src="https://www.youtube.com/embed/N4bZNW1D6_4" 
frameborder="0" 
allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" 
allowfullscreen></iframe>


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
