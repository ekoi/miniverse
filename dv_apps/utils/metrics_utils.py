import StringIO
import pandas as pd
from django.http import HttpResponse

AUDIENCE = {"D20000": "Life sciences, medicine and health care", "D30000": "Humanities", "D33000": "Theology and religious studies", "D34000": "History",
            "D34300": "Modern and contemporary history", "D36000": "Language and literature studies",
            "D37000": "Archaeology", "D41000": "Science of law", "D41300": "Criminal (procedural) law and criminology",
            "D50000": "Behavioural and educational sciences", "D51000": "Psychology", "D60000": "Social sciences", "D61000": "Sociology",
            "D63000": "Cultural anthropology", "D64000": "Demography", "D64000": "Demography", "D70000": "Economics and Business Administration"}


def get_easy_excel_sheets(parameters, graphs, name):

    excel_string_io = StringIO.StringIO()
    pd_writer = pd.ExcelWriter(excel_string_io, engine='xlsxwriter')

    columns = list(parameters.keys())
    data = [parameters]
    df = pd.DataFrame(data, columns=columns)
    df.to_excel(pd_writer, index=False, sheet_name='Parameters', columns=columns)

    columns = ['yyyy_mm', 'count', 'running_total']
    for graph in graphs:
        df = pd.DataFrame(graph['data'], columns=columns)
        df.to_excel(pd_writer, index=False, sheet_name=graph['name'], columns=columns)

    pd_writer.save()
    excel_string_io.seek(0)
    workbook = excel_string_io.getvalue()


    if workbook is None:
        # Ah, make a better error
        return HttpResponse('Sorry! An error occurred trying to create an Excel spreadsheet.')

    response = HttpResponse(workbook, \
                            content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')

    response['Content-Disposition'] = 'attachment; filename=%s' % name

    return response