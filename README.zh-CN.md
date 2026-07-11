# T.E.S.T. — 可追溯证据综合工具包

<p align="center">
  <strong>把模糊问题转化为有来源、可核验、可决策的研究简报。</strong><br>
  一个适用于调研、比较、核查、文献综述与时效性信息分析的通用 Agent Skill。
</p>

<p align="center">
  <a href="README.md">English</a> ·
  <a href="skills/traceable-research/SKILL.md">Skill 指令</a> ·
  <a href="CONTRIBUTING.md">参与贡献</a>
</p>

---

## 为什么做 T.E.S.T.？

很多低质量研究并不是写作能力不够，而是研究流程从一开始就有问题：没有先定义问题，拿搜索摘要当证据，只引用二手转述，忽略互相冲突的材料，或者先写结论再补引用。

**T.E.S.T.** 把研究过程变成一条清晰、可审计的流水线：

```text
问题 → 范围 → 来源地图 → 来源账本 → 主张账本
     → 冲突检查 → 引用审计 → 可决策简报
```

它不限定具体领域，可用于：

- 产品、软件、服务和方案比较；
- 科研与技术文献综述；
- 市场、政策、公司和行业调研；
- 事实核查与说法验证；
- 旅行、兴趣爱好和个人选择；
- 任何强调时效性、不确定性或证据冲突的任务。

## 它为什么不只是一段提示词

- **清晰的触发边界**：明确什么时候使用、什么时候不使用。
- **可重复的流程**：十个研究阶段，带停止条件和质量门槛。
- **证据模型**：同时处理来源质量、主张状态、独立性、时效性和冲突。
- **实用脚本**：零第三方依赖的 Python 工具，可创建工作区并审计研究产物。
- **渐进式加载**：核心指令保持紧凑，细节放在按需读取的参考文件和模板中。
- **评测材料**：中英文触发测试与输出质量测试。
- **多客户端兼容**：遵循 Agent Skills 结构，同时提供 Claude 与 Codex 插件清单。
- **自动化验证**：CI 检查脚本、清单、引用与 Skill 结构。

## 快速安装

### 使用通用 Skills CLI

```bash
npx skills add Tq-1/test --skill traceable-research
```

### Claude Code

```text
/plugin marketplace add Tq-1/test
/plugin install traceable-research@tq1-skills
```

### Codex

```bash
codex plugin marketplace add Tq-1/test
```

然后在插件目录搜索 **T.E.S.T.** 并安装。

### 手动安装

将自包含目录 [`skills/traceable-research`](skills/traceable-research) 复制到你所使用的 Agent 的 skills 目录中。

## 使用示例

```text
请用 T.E.S.T. 比较几款适合五人科研团队的本地优先笔记软件。
区分已核实事实与推断，注明价格核验日期，并给出一个明确推荐。
```

复杂任务可先初始化工作区：

```bash
python skills/traceable-research/scripts/init_workspace.py \
  "哪款本地优先笔记软件最适合五人科研团队？" \
  --mode standard \
  --out research/note-apps
```

填写来源账本、主张账本和简报后进行审计：

```bash
python skills/traceable-research/scripts/audit_research.py research/note-apps --strict
```

验证仓库本身：

```bash
python skills/traceable-research/scripts/validate_skill.py .
python -m unittest discover -s tests -v
```

## 四种研究模式

| 模式 | 适用场景 | 默认要求 |
|---|---|---|
| `quick` | 低风险问题、快速摸底 | 少量直接且较新的来源 |
| `standard` | 大多数比较与报告 | 一手来源 + 独立反证来源 |
| `deep` | 文献综述、战略判断 | 更广覆盖、明确说明饱和度和冲突 |
| `high-stakes` | 法律、医疗、金融、安全或不可逆决策 | 官方/一手证据、更强交叉验证、明确局限 |

来源数量是目标，不是凑数指标。当新增材料不再改变结论、已经触及证据上限，或达到约定研究预算时，应停止继续搜索。

## 完成标准

一份合格的 T.E.S.T. 简报应当让读者快速回答：

1. 一段话结论是什么？
2. 哪些主张属于已核实、受支持、有争议、推断或未解决？
3. 每个重要主张由哪些来源直接支持？
4. 证据核验到什么日期？
5. 处理冲突证据后，结论发生了什么变化？
6. 读者下一步应该做什么？
7. 哪条新证据最可能改变当前建议？

内置审计器负责检查结构和引用关系，但它不能替代研究者对来源真实性和结论合理性的判断。

## 设计原则

- 先证据，后行文
- 先一手，后二手
- 先主张，后结论
- 先冲突，后置信
- 先日期，再谈“最新”
- 先审计，再交付
- 不确定性必须显式表达

## 仓库故事

这个仓库原本是 Tq-1 在 2021 年创建的第一个小型 GitHub 测试仓库。现在它被正式重构为 **T.E.S.T.**，原始说明保存在 [`HISTORY.md`](HISTORY.md) 中。新的名称代表 **Traceable Evidence Synthesis Toolkit（可追溯证据综合工具包）**。

## 许可证

MIT，详见 [`LICENSE`](LICENSE)。
