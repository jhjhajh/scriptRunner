import mongoose from 'mongoose'
import validator from 'validator'

const UserSchema = new mongoose.Schema({
    username: {
        type:String,
        required: [true, 'Please input username'],
        validate: {
            validator: validator.isEmail,
            message: 'Please provide a valid email',
        },
        minlength:3,
        maxlength:20,
        trim: true,
    },
    password:{
        type:String,
        required: [true, 'Please input password']
    },
})

// UserSchema.methods.createJWT = function() {
//     console.log(this)
// }
export default mongoose.model('User',UserSchema)