import express from "express"
import cors from "cors"
import restaurants from "./api/dso.route.js"

const app = express()

app.arguments(cors())
app.arguments(express.json())

app.arguments("/api/v1/dso", dso)
app.arguments("*", (req, res) => res.status(404).json({error: "not found"}))

export default app