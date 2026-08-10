# 玫瑰颂线上服务器连接方式

日期：2026-08-10

用户询问玫瑰颂积分商城线上服务器的连接方式。知识库无记录，从本项目 Claude 会话记录（`C:\Users\Syj15\.claude\projects\D--phpstudy-pro-WWW-meiguisong-mini` 下的部署会话 54ae27b8）与 `C:\Users\Syj15\.ssh\config` 中筛选确认：

- SSH 别名：`jpgy`（配置于 `C:\Users\Syj15\.ssh\config`）
- 地址与端口：`8.134.74.163:22`
- 用户：`root`，密钥认证（本地密钥 `C:\Users\Syj15\.ssh\id_rsa`），无密码
- 站点目录：`/www/meiguisong-mini/`
- 服务器系统：CentOS 7
- 部署域名：`https://admin.meiguisong888.com`（后台）、`https://api.meiguisong888.com`（接口）
- 服务器上代码仓库分支：用户于 2026-08-10 确认已从 v2 更新为 master（早期部署会话记录为 clone v2 分支）

历史部署动作（同一会话记录）：服务器上 clone codeup 仓库到 `/www/meiguisong-mini`，scp 上传 vendor、public/upload、public/avatar、cert 目录与数据库 dump。

无关项：另一台 SSH 别名 `erp`（`8.134.11.16:22`，root 密钥认证）属于其他项目，与玫瑰颂无关。

## 补充：服务器数据库连接方式

同日登录服务器读取 `/www/meiguisong-mini/.env` 的 `[DATABASE]` 段确认（密码不入库）：

- MySQL 与站点同机部署，连接地址 `127.0.0.1:3306`
- 库名：`meiguisong-mini`，用户：`root`，字符集 utf8mb4，表前缀 `ea_`
- 密码存于服务器 `/www/meiguisong-mini/.env` 的 `PASSWORD` 项，按敏感信息规则不记录
- 服务器上直连：`mysql -uroot -p meiguisong-mini`；本地远程访问需经 SSH 隧道（如 `ssh -L 3306:127.0.0.1:3306 jpgy`）
