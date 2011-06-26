from django.http import HttpResponse
import csv

class CsvExport:
    csv_export_url = '~csv/'
    csv_export_dialect = 'excel'
    csv_follow_relations = []
    csv_export_fmtparam = {
       'delimiter': ',',
       'quotechar': '"',
       'quoting': csv.QUOTE_ALL,
    }
    
    def csv_export(self, queryset):

        if len(queryset) < 1:
            return HttpResponse("No data", status=204);

        model = queryset.model
        fields = self.get_csv_export_fields(model)
        headers = [self.csv_get_fieldname(f) for f in fields]
        
        #response = HttpResponse(mimetype='text/plain')
        response = HttpResponse(mimetype='text/csv')
        response['Content-Disposition'] = 'attachment; filename=%s' % self.csv_get_export_filename(model)
        writer = csv.writer(response, self.csv_export_dialect, **self.csv_export_fmtparam)
        writer.writerow(headers)
        for row in queryset:
            csvrow = [f.encode('utf-8') if isinstance(f, unicode) else f for f in [self.csv_resolve_field(row, f) for f in fields]]
            writer.writerow(csvrow)
        return response
        
    def get_csv_export_fields(self, model):
        """
        Return a sequence of tuples which should be included in the export.
        """
        fields = [f.name for f in model._meta.fields]
        for relation in self.csv_follow_relations:
            for field in model._meta.get_field_by_name(relation)[0].rel.to._meta.fields:
                fields.append([relation, field.name])
        return fields
    
    def csv_get_export_filename(self, model):
        return '%s_export.csv' % (model._meta.module_name)

    def csv_resolve_field(self, row, fieldname):
        if isinstance(fieldname, basestring):
            return getattr(row, fieldname)
        else:
            obj = row
            for bit in fieldname:
                obj = getattr(obj, bit)
            return obj
        
    def csv_get_fieldname(self, field):
        if isinstance(field, basestring):
            return field
        return '.'.join(field)
