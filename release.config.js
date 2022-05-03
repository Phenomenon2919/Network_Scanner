module.exports = {
    branches: ["master", "beta"],
    repositoryUrl: "https://github.com/Phenomenon2919/Network_Scanner",
    plugins: [
        '@semantic-release/commit-analyzer',
        '@semantic-release/release-notes-generator',
        ['@semantic-release/github',{
            "assets": [
                {"path":"dist/network_scanner","name":"Simple Network Scanner","label":"Executable Network Scanner"}
            ]
        }]
    ]
}