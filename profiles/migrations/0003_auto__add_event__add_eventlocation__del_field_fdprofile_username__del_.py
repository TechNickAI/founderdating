# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Event'
        db.create_table('profiles_event', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('event_date', self.gf('django.db.models.fields.DateField')()),
            ('event_location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.EventLocation'])),
        ))
        db.send_create_signal('profiles', ['Event'])

        # Adding model 'EventLocation'
        db.create_table('profiles_eventlocation', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('display', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('profiles', ['EventLocation'])

        # Deleting field 'FdProfile.username'
        db.delete_column('profiles_fdprofile', 'username')

        # Deleting field 'FdProfile.last_login'
        db.delete_column('profiles_fdprofile', 'last_login')

        # Deleting field 'FdProfile.is_active'
        db.delete_column('profiles_fdprofile', 'is_active')

        # Adding field 'FdProfile.event'
        db.add_column('profiles_fdprofile', 'event', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['profiles.Event'], null=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'Event'
        db.delete_table('profiles_event')

        # Deleting model 'EventLocation'
        db.delete_table('profiles_eventlocation')

        # Adding field 'FdProfile.username'
        db.add_column('profiles_fdprofile', 'username', self.gf('django.db.models.fields.CharField')(default='', max_length=100), keep_default=False)

        # Adding field 'FdProfile.last_login'
        db.add_column('profiles_fdprofile', 'last_login', self.gf('django.db.models.fields.DateTimeField')(default=datetime.date(2011, 4, 17), blank=True), keep_default=False)

        # Adding field 'FdProfile.is_active'
        db.add_column('profiles_fdprofile', 'is_active', self.gf('django.db.models.fields.BooleanField')(default=True), keep_default=False)

        # Deleting field 'FdProfile.event'
        db.delete_column('profiles_fdprofile', 'event_id')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'profiles.event': {
            'Meta': {'object_name': 'Event'},
            'event_date': ('django.db.models.fields.DateField', [], {}),
            'event_location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.EventLocation']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'profiles.eventlocation': {
            'Meta': {'object_name': 'EventLocation'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'display': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'profiles.fdprofile': {
            'Meta': {'object_name': 'FdProfile'},
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.Event']", 'null': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mugshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'privacy': ('django.db.models.fields.CharField', [], {'default': "'registered'", 'max_length': '15'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': "orm['auth.User']"})
        }
    }

    complete_apps = ['profiles']
