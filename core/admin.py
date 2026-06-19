from django.contrib import admin
from django.http import HttpResponse
from django.utils.html import escape

from .models import Enter


@admin.register(Enter)
class EnterAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'phone')
    search_fields = ('username', 'phone')
    ordering = ('-id',)

    def changelist_view(self, request, extra_context=None):
        entries = Enter.objects.order_by('-id')
        rows = ''.join(
            '<tr>'
            f'<td>{entry.id}</td>'
            f'<td>{escape(entry.username)}</td>'
            f'<td>{escape(entry.phone)}</td>'
            '</tr>'
            for entry in entries
        )
        if not rows:
            rows = '<tr><td colspan="3" class="empty">暂无注册数据</td></tr>'

        return HttpResponse(f'''
<!doctype html>
<html lang="zh-hans">
<head>
  <meta charset="utf-8">
  <title>注册表单</title>
  <style>
    body {{
      margin: 0;
      padding: 32px;
      color: #1f2933;
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
      background: #f7f9fc;
    }}
    .panel {{
      max-width: 980px;
      margin: 0 auto;
      background: #fff;
      border: 1px solid #e5eaf0;
      border-radius: 8px;
      box-shadow: 0 12px 30px rgba(31, 41, 51, 0.08);
      overflow: hidden;
    }}
    .header {{
      padding: 24px 28px;
      border-bottom: 1px solid #edf1f5;
    }}
    h1 {{
      margin: 0;
      font-size: 24px;
      font-weight: 700;
    }}
    .meta {{
      margin-top: 8px;
      color: #66788a;
      font-size: 14px;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
    }}
    th, td {{
      padding: 16px 28px;
      border-bottom: 1px solid #edf1f5;
      text-align: left;
      font-size: 15px;
    }}
    th {{
      background: #f2f6fb;
      color: #334e68;
      font-weight: 700;
    }}
    tr:last-child td {{
      border-bottom: 0;
    }}
    .empty {{
      color: #829ab1;
      text-align: center;
    }}
  </style>
</head>
<body>
  <section class="panel">
    <div class="header">
      <h1>注册表单</h1>
      <div class="meta">共 {entries.count()} 条真实提交数据</div>
    </div>
    <table>
      <thead>
        <tr>
          <th>ID</th>
          <th>用户名</th>
          <th>电话</th>
        </tr>
      </thead>
      <tbody>{rows}</tbody>
    </table>
  </section>
</body>
</html>
''')
