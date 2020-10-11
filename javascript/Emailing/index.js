// NOTE: Make sure to fill out the info in config.json and email.json before running
const nodemailer = require("nodemailer");
const configuration = require("./config.json");

var transporter = nodemailer.createTransport({
    service: 'gmail',
    auth: configuration
});

var mail_opts = require("./email.json");
mail_opts["from"] = configuration["user"];

transporter.sendMail(mail_opts, (error, info) => {
    if (error) {
        console.error(error);
    } else {
      console.log(`Email was successfully sent to ${mail_opts["to"]}`);
    }
});