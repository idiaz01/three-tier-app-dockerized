db = getSibling('application')
db.createUser(
    {
        user: "flask_api",
        pwd: "anotherpassword",
        roles: [
            {
                role: "readWrite",
                db: "application"
            }
        ]
    }
);