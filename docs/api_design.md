# API design

## Quiz

### Create

Method: `POST`

URL: `/api/quiz`

Payload: [`Quiz`](#quiz)

Return value: [`Quiz`](#quiz)

### Read

Method: `GET`

URL: `/api/quiz`

Return value: [`[Quiz]`](#quiz)

### Read (single)

Method: `GET`

URL: `/api/quiz/{id}`

Parameters: `id: string`

Return value: [`Quiz`](#quiz)

### Update

Method: `PUT`

URL: `/api/quiz/{id}`

Parameters: `id: string`

Payload: [`Quiz`](#quiz)

Return value: [`Quiz`](#quiz)

### Delete

Method: `DELETE``

URL: `/api/quiz/{id}`

Parameters: `id: string`



## Data Types

<a name="quiz"></a>

```json
Quiz {
    title: string,
    questions: [Question]
}
```

<a name="question"></a>

```json
Question {
    question: string,
    answers: [Answer]
}
```

<a name="answer"></a>

```json
Answer {
    answer: string,
    isCorrect: boolean
}
```

