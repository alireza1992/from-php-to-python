| Step          | What if it fails?        | Rollback? | Retry?                           | Ignore?        |
| ------------- |--------------------------|-----------|----------------------------------|----------------|
| Save Player   | Whole logic fails        | Yes       | Depends on which phase it failed | No             |
| Send Email    | Doesn't matter that much | No        | Yes, in the queue                | Preferably not |
| Generate JWT  | Endpoint will need it    | -         | Yes                              | No             |
| Hash Password | Can't happen             | -         | Yes                              | No             |



## What can go wrong ?:

1- Database timeout

2- Database connection failure

3- Duplicate email

4- Validation error

5- Deadlock


## Who owns the recovery:

1- Database

2- Client/User

3- Support

4- Retry (queue)

5- Code

