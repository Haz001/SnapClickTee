import base64
import dataclasses
from enum import StrEnum

import gradio_client
from io import BytesIO
import json
import requests

from flask import Request

from apps import app

client = gradio_client.Client("https://lambdalabs-image-mixer-demo.hf.space/")


def single_img():
    response = requests.post("https://trysem-sd-2-1-img2img.hf.space/run/predict", json={
        "data": [
            "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAACklEQVR4nGMAAQAABQABDQottAAAAABJRU5ErkJggg==",
            "hello world",
            "hello world",
            7,
            10,
            202908330402049540,
            0.5,
        ]}).json()

    data = response["data"]


@dataclasses.dataclass
class Slot:
    class InputTypes(StrEnum):
        Image = "Image"
        Text = "Text/URL"
        Nothing = "Nothing"

    inputType: InputTypes = InputTypes.Nothing
    prompt: str = "Cute Kittens"
    imageUrl: str = "https://placehold.co/1920x1080.png?text=Hello+World&font=roboto"
    strength: float = 1


def slot_limit(slots: list[Slot]) -> list[Slot]:
    if len(slots) < 1:
        slots.append(Slot(inputType=Slot.InputTypes.Nothing))
    else:
        while len(slots) > 5:
            slots.pop()
    return slots


def image_merge(slot1: Slot, slot2: Slot = Slot(), slot3: Slot = Slot(), slot4=Slot(), slot5=Slot()):
    result = client.predict(
        slot1.inputType.value,
        slot2.inputType.value,
        slot3.inputType.value,
        slot4.inputType.value,
        slot5.inputType.value,
        slot1.prompt,
        slot2.prompt,
        slot3.prompt,
        slot4.prompt,
        slot5.prompt,
        slot1.imageUrl,
        slot2.imageUrl,
        slot3.imageUrl,
        slot4.imageUrl,
        slot5.imageUrl,
        slot1.strength,
        slot2.strength,
        slot3.strength,
        slot4.strength,
        slot5.strength,
        10,  # int | float (numeric value between 1 and 10) in 'CFG scale' Slider component
        1,  # int | float (numeric value between 1 and 1) in 'Num samples' Slider component
        1,  # int | float (numeric value between 0 and 10000) in 'Seed' Slider component
        90,  # int | float (numeric value between 10 and 100) in 'Steps' Slider component
        fn_index=5
    )
    print(f"{result}")
    jf = open(f"{result}/captions.json", 'r')
    text = jf.read()
    jf.close()
    filepath = list(json.loads(text).keys())[0]
    buf: BytesIO
    print(filepath)
    with open(filepath, "rb") as img:
        buf = BytesIO(img.read())
    del text
    del jf
    del filepath
    return buf


clamp: callable = lambda number, minimum, maximum: max(min(maximum, number), minimum)


@app.route("/merge", method="POST")
def api_image_merge():
    slots: list[Slot] = list()
    if Request.is_json:
        # noinspection PyTypeChecker
        data: list[dict[str, int | str]] = Request.json
        for slot_num in clamp(len(data), 0, 5):
            d_slot: dict[str, int | str] = data[slot_num]
            slot: Slot = Slot(inputType=Slot.InputTypes.Nothing)
            if d_slot["type"].lower() == "image":
                slot.inputType = Slot.InputTypes.Image
                if "url" in d_slot:
                    slot.imageUrl = d_slot["url"]
                else:
                    return "JSON malformed", 400
                if "prompt" in d_slot:  # API allows it
                    slot.prompt = d_slot["prompt"]
                if "strength" in d_slot:
                    slot.strength = d_slot["strength"]
            elif d_slot["type"].lower() == "text":
                slot.inputType = Slot.InputTypes.Text
                if "prompt" in d_slot:
                    slot.prompt = d_slot["prompt"]
                else:
                    return "JSON malformed", 400
                if "url" in d_slot:  # API allows it
                    slot.imageUrl = d_slot["url"]
                if "strength" in d_slot:
                    slot.strength = d_slot["strength"]
            slots.append(slot)
    else:
        # noinspection PyTypeChecker
        data: dict[str, str] = Request.form
        for i in range(len(5)):
            t_slot: Slot = Slot()
            if (f"input{i}" in data):
                type = data[f"input{i}"].lower()
                if type == "image" or type == "text":


if __name__ == "__main__":
    img: BytesIO = image_merge(
        slot1=Slot(
            inputType=Slot.InputTypes.Image,
            imageUrl="https://raw.githubusercontent.com/Haz001/SnapClickTee/main/apps/static/img/Bridge%20and%20Plants%20-%20Mayfly%20Pub.jpg?token=GHSAT0AAAAAACIRO6LCHI7WVWTVUWMTHDZEZKKWTEA",
        ),
        slot2=Slot(
            inputType=Slot.InputTypes.Text,
            prompt="black and white, old"

        )
    )
    pilimg = Image.open(img)
    pilimg.show("AI Art")
    pilimg = pilimg.resize((300,300))
    data: BytesIO = BytesIO()
    pilimg.save(data,format="PNG")
    print(base64.encodebytes(data.getvalue()))
