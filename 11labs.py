import elevenlabs

audio = elevenlabs.generate(
    text="Hello adventurer! What shall we do today?", voice="Daniel"
)

elevenlabs.play(audio)
