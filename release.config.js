module.exports = {
    branches: ["master", "beta"],
    repositoryUrl: "https://github.com/Phenomenon2919/Network_Scanner",
    plugins: [
        '@semantic-release/commit-analyzer',
        '@semantic-release/release-notes-generator',
        '@semantic-release/github',
        ["@semantic-release/git", {
            "assets": ["dist/network_scanner"]
            // "message": "chore(release): ${nextRelease.version} [skip ci]\n\n${nextRelease.notes}"
          }]
    ]
}