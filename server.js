import express from 'express'
const app = express()
import dotenv from 'dotenv'
dotenv.config()
import 'express-async-errors'
import morgan from 'morgan'
// db and authenticateUser
import connectDB from './db/connect.js'

//routers
import authRouter from './routes/authRoutes.js'
import jobsRouter from './routes/jobsRoutes.js'
// import MONGO_URL from '.env'

//middleware
import notFoundMiddleware from './middleware/not-found.js'
import errorHandlerMiddleware from './middleware/error-handler.js'

if (process.env.NODE_ENV !== 'production') {
    app.use(morgan('dev'))
}

app.use(express.json())
// console.log("hello")
app.get('/', (req,res)=>{
    // throw new Error('error')
    res.send('Welcome!')
})

app.use('/api/v1/auth', authRouter)
app.use('/api/v1/jobs', jobsRouter)


app.use(notFoundMiddleware)
app.use(errorHandlerMiddleware)
const port = process.env.PORT || 5000
const MONGO_URL="mongodb://127.0.0.1:27017/admin"
const start = async ()=>{
    try {
        // await connectDB (process.env.MONGO_URL)
        // await connectDB("localhost:27017/admin")
        (async () => {
            try {
                await connectDB (MONGO_URL, {
                    useNewUrlParser: true,
                    useUnifiedTopology: true,
                    useFindAndModify: false,
                    useCreateIndex: true
                });
                console.log(`MongoDB Connected: ${MONGO_URL}`);
            } catch (err) {
                console.error(err);
            }
        })();
        app.listen(port,()=>{
            console.log(`Server is listening on port ${port}...`)
        }) 
    } catch (error) {
        console.log(error);

    }
}

start()