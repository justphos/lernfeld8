import com.jetbrains.rd.platform.ktor.client.*
import com.jetbrains.rd.platform.ktor.client.call.*
import com.jetbrains.rd.platform.ktor.client.request.*
import com.jetbrains.rd.platform.ktor.client.util.*
import com.jetbrains.rd.util.reactive.*
import com.jetbrains.rd.util.string.*
import kotlinx.serialization.json.*

fun main() {
    val api = ApiClient("https://api.github.com")
    val token = "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"
    val owner = "justphos"
    val repo = "lernfeld8"

    api.setCredentials(UsernamePasswordCredentials(token, "x-oauth-basic"))

    val workflow = """
        name: Lernfeld 8 Continuous-Delivery-Pipeline

        on:
          push:
            branches: [ "main" ]
          pull_request:
            branches: [ "main" ]

        permissions:
          contents: read

        jobs:
          build:
            runs-on: ubuntu-latest

            steps:
            - uses: actions/checkout@v3
            - name: Python 3.10 Setup
              uses: actions/setup-python@v3
              with:
                python-version: "3.10"
            - name: Install dependencies
              run: |
                python -m pip install --upgrade pip
                pip install flake8 pytest
                if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
            - name: Lint code with flake8
              run: |
                flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics
                flake8 . --count --exit-zero --max-complexity=10 --max-line-length=127 --statistics
            - name: Run unit tests with pytest
              run: pytest
            - name: Generate test coverage report
              run: |
                pip install coverage
                coverage run -m pytest
                coverage report -m
                coverage html
    """.trimIndent()

    val createWorkflowResponse = api.workflows.create(owner, repo, body = CreateWorkflow(workflow)).execute()
    println("Workflow created: ${createWorkflowResponse.status.isSuccess()}")
}

