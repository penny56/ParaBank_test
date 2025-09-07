 我现在要写一个github repo的 readme.md，主要有以下几条：
1. 我习惯用python，对 Typescript or Javascript 不是特别的熟悉，但是我可以最快速度上手。
2. UI test 与 API test 2 个 test case 位于 tests/ui/test_ui_flow.py 与 tests/ui/test_api_flow.py。其中，我们需要先执行test_ui_flow.py，它会把 step8 的 bill pay 信息写成 json文件，放在项目根目录，同时也会把登录cookie信息保存在同样位置的json文件。在执行test_api_flow.py时，会用到 cookie 与 step8 的 bill pay 信息参与验证。

下面是2个 test scenarios 的一些细节：
- UI Test scenarios，使用 BasePage 作为父类，每种page作为子类，当转到不同page时，会创建不同page的类对象，并通过操作类的成员函数进行操作，比如 RegisterPage 类，

整个验证工作是由 pytest module 完成，如果2个test case 执行成功会输出：
- UI Test scenarios: completed!
- API Test scenarios: completed!

CI/CD 工作是由 