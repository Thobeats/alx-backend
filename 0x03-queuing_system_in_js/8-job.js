function createPushNotificationsJobs(jobs, queue)
{
    if (!Array.isArray(jobs)) throw Error('Jobs is not an array');

    for (const job of jobs) {
        let jobData = {
            phoneNumber: job.phoneNumber,
            message: job.message,
        }

        const _job = queue.create('push_notification_code_3', jobData)
                    .save((err) => {
                        if (!err) console.log(`Notification job created: ${_job.id}`);
                    })
        _job.on('complete', () => console.log(`Notification job ${_job.id} completed`));
        _job.on('failed', (err) => console.log(`Notification job ${_job.id} failed: ${err}`));
        _job.on('progress', (progress) => console.log(`Notification job ${_job.id} ${progress}% complete`));
    }
}

module.exports = createPushNotificationsJobs;