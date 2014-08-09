github-topics-analyzer
======================

![](https://travis-ci.org/microhackaton/github-topics-analyzer.svg)

##### Port

8911

##### In

`/api/analyze`

Method: POST
```
{
    "pairId" : "1",
    "githubId" : "marcin",
    "repos" : {
       // Zgodne z https://api.github.com/users/:githubId/repos
    ],
    "orgs": [
       // Zgodne z https://api.github.com/users/:githubId/orgs
    ]
}
```

Odpowiedź:
* 202 Accepted
* 400 Bad Request - gdy brak body

##### Out

{

    "pairId" : "1",
    "analyzerType" : "github",
    "analyzedId" : "marcin",
    "topics" :
    [
       {
        "name":"C"
       },
       { "
        name":"Python"
       }
   ]
}
