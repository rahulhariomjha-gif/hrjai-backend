from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routers.auth as auth
import routers.pdf as pdf
import routers.image as image
import routers.video as video
import routers.ai as ai
import routers.payment as payment
import routers.admin as admin

app = FastAPI(title="HRJ AI Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(auth.router, prefix="/auth")
app.include_router(pdf.router, prefix="/pdf")
app.include_router(image.router, prefix="/image")
app.include_router(video.router, prefix="/video")
app.include_router(ai.router, prefix="/ai")
app.include_router(payment.router, prefix="/payment")
app.include_router(admin.router, prefix="/admin")

@app.get("/")
async def home():
    return {"status": "HRJ AI Backend Running!"}
