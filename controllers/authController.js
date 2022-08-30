import User from "../models/User.js"
import {StatusCodes} from 'http-status-codes'
import { BadRequestError} from '../errors/index.js'

const register = async (req, res, next) => {
const {username,password} = req.body
if(!username || !password) {
    throw new BadRequestError('Please provide valid input for all fields!')
}
        const user = await User.create({username, password})
        res.status(StatusCodes.OK).json({user})

}
const login = async (req, res) => {
    const { username, password } = req.body
    if (!username || !password) {
        throw new BadRequestError('Please input username and password')
    }

    if (username === "admin" && password === "admin") {
        //token thingy
    }
    // res.send ('login user')
}

const updateUser = async (req, res) => {
    res.send ('updateUser')
}

export {login, updateUser}