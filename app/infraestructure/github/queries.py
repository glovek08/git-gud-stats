GET_USER_DATA = """
    query($login: String!) {
        user(login: $login) {
        name
        login
        avatarUrl
        repositories(first: 50, orderBy: {field: STARGAZERS, direction: DESC}, isFork: false, isArchived:false, privacy: PUBLIC) {
            nodes {
            name
            diskUsage
            languages(first: 10, orderBy: {field: SIZE, direction: DESC}) {
                edges {
                size
                node {
                    name
                }
                }
            }
            }
        }
        }
    }
"""
