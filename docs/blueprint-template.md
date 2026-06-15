# Day 13 Observability Lab Report

> **Instruction**: Fill in all sections below. This report is designed to be parsed by an automated grading assistant. Ensure all tags (e.g., `[GROUP_NAME]`) are preserved.

## 1. Team Metadata
- [GROUP_NAME]: Mai Đức Vinh Solo
- [REPO_URL]: https://github.com/ducvinh101101/2A202600587-MaiDucVinh-Day13
- [MEMBERS]:
  - Member A: Mai Đức Vinh | Role: Fullstack (Logging, PII, Tracing, Alerts, Report)

---

## 2. Group Performance (Auto-Verified)
- [VALIDATE_LOGS_FINAL_SCORE]: 100/100
- [TOTAL_TRACES_COUNT]: > 10 traces
- [PII_LEAKS_FOUND]: 0

---

## 3. Technical Evidence (Group)

### 3.1 Logging & Tracing
- [EVIDENCE_CORRELATION_ID_SCREENSHOT]: screenshots/correlation_id.png
- [EVIDENCE_PII_REDACTION_SCREENSHOT]: screenshots/pii_redaction.png
- [EVIDENCE_TRACE_WATERFALL_SCREENSHOT]: screenshots/trace_waterfall.png
- [TRACE_WATERFALL_EXPLANATION]: Trace ghi nhận quá trình request đi từ tầng API xuống logic agent, truy xuất (retrieve) và gọi mô hình (generate). Việc gắn Correlation ID giúp kết nối các span, từ đó ta dễ dàng phân tích độ trễ tại từng công đoạn (như phần `retrieve` bị chậm khi giả lập lỗi).

### 3.2 Dashboard & SLOs
- [DASHBOARD_6_PANELS_SCREENSHOT]: screenshots/dashboard.png
- [SLO_TABLE]:
| SLI | Target | Window | Current Value |
|---|---:|---|---:|
| Latency P95 | < 3000ms | 28d | OK |
| Error Rate | < 2% | 28d | OK |
| Cost Budget | < $2.5/day | 1d | OK |

### 3.3 Alerts & Runbook
- [ALERT_RULES_SCREENSHOT]: screenshots/alerts.png
- [SAMPLE_RUNBOOK_LINK]: docs/alerts.md#1-high-latency-p95

---

## 4. Incident Response (Group)
- [SCENARIO_NAME]: rag_slow
- [SYMPTOMS_OBSERVED]: Hệ thống bị timeout hoặc độ trễ phản hồi cực cao (> 5 giây) khi user gửi request `/chat` với feature "qa".
- [ROOT_CAUSE_PROVED_BY]: Phân tích Trace trên Langfuse cho thấy span giả lập `mock_rag` (hàm retrieve) là nút thắt cổ chai, chiếm toàn bộ độ trễ.
- [FIX_ACTION]: Vô hiệu hóa tính năng lỗi giả lập bằng API `/incidents/rag_slow/disable`.
- [PREVENTIVE_MEASURE]: Thiết lập circuit breaker và hard timeout (ví dụ: tối đa 2000ms) cho service RAG. Triển khai fallback message nếu RAG phản hồi quá chậm để đảm bảo trải nghiệm người dùng.

---

## 5. Individual Contributions & Evidence

### Mai Đức Vinh
- [TASKS_COMPLETED]: 
  1. Cấu hình middleware Correlation ID & Log Enrichment.
  2. Áp dụng PII scrubber (Redact email, phone, cccd, passport, địa chỉ, biển số xe).
  3. Tích hợp Langfuse decorator để tracing.
  4. Hoàn thiện Alert Rules và Dashboard Blueprint.
- [EVIDENCE_LINK]: Xem toàn bộ các file đã commit trong thư mục `app/` và `config/` (Repo 2A202600587-MaiDucVinh-Day13).

---

## 6. Bonus Items (Optional)
- [BONUS_COST_OPTIMIZATION]: Đã thêm theo dõi số lượng token và giá trị quy đổi chi phí (USD) trên từng request log, từ đó tạo alert rule báo cáo chi tiêu tăng đột biến `cost_budget_spike`.
- [BONUS_AUDIT_LOGS]: N/A
- [BONUS_CUSTOM_METRIC]: N/A
