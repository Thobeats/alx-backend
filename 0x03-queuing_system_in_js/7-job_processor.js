const kue = require('kue');
const queue = kue.createQueue();

const blacklisted = ['4153518780', '4153518781'];

function sendNotification(phoneNumber, message, job, done) {
    const total = 100;
    function next(p) {
        if (p === 0 || p === (total / 2)) {
            job.progress(p, total);
            if (p === (total / 2)) {
                console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
            }
        }
        if (blacklisted.includes(job.data.phoneNumber)) {
            return done(new Error(`Phone number ${job.data.phoneNumber} is blacklisted`));
        }
        if (p === total) {
            return done();
        }
        return next(p + 1);
    }
    next(0);
}

const job_listener = queue.process('push_notification_code_2', (job, done) => {
    sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
