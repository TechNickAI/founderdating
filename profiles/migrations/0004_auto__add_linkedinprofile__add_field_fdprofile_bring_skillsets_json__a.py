# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'LinkedinProfile'
        db.create_table('profiles_linkedinprofile', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fd_profile', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['profiles.FdProfile'], unique=True)),
            ('oauth_object', self.gf('django.db.models.fields.TextField')(max_length=500)),
            ('profile_raw', self.gf('django.db.models.fields.TextField')()),
            ('profile_picture', self.gf('django.db.models.fields.URLField')(max_length=200, null=True, blank=True)),
            ('profile_location', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('profile_industry', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal('profiles', ['LinkedinProfile'])

        # Adding field 'FdProfile.bring_skillsets_json'
        db.add_column('profiles_fdprofile', 'bring_skillsets_json', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FdProfile.need_skillsets_json'
        db.add_column('profiles_fdprofile', 'need_skillsets_json', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True), keep_default=False)

        # Adding field 'FdProfile.past_experience_blurb'
        db.add_column('profiles_fdprofile', 'past_experience_blurb', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FdProfile.bring_blurb'
        db.add_column('profiles_fdprofile', 'bring_blurb', self.gf('django.db.models.fields.TextField')(null=True, blank=True), keep_default=False)

        # Adding field 'FdProfile.can_start'
        db.add_column('profiles_fdprofile', 'can_start', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True), keep_default=False)

        # Adding field 'FdProfile.idea_status'
        db.add_column('profiles_fdprofile', 'idea_status', self.gf('django.db.models.fields.CharField')(max_length=25, null=True, blank=True), keep_default=False)

        # Adding field 'FdProfile.event_status'
        db.add_column('profiles_fdprofile', 'event_status', self.gf('django.db.models.fields.CharField')(default='Pending', max_length=25), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'LinkedinProfile'
        db.delete_table('profiles_linkedinprofile')

        # Deleting field 'FdProfile.bring_skillsets_json'
        db.delete_column('profiles_fdprofile', 'bring_skillsets_json')

        # Deleting field 'FdProfile.need_skillsets_json'
        db.delete_column('profiles_fdprofile', 'need_skillsets_json')

        # Deleting field 'FdProfile.past_experience_blurb'
        db.delete_column('profiles_fdprofile', 'past_experience_blurb')

        # Deleting field 'FdProfile.bring_blurb'
        db.delete_column('profiles_fdprofile', 'bring_blurb')

        # Deleting field 'FdProfile.can_start'
        db.delete_column('profiles_fdprofile', 'can_start')

        # Deleting field 'FdProfile.idea_status'
        db.delete_column('profiles_fdprofile', 'idea_status')

        # Deleting field 'FdProfile.event_status'
        db.delete_column('profiles_fdprofile', 'event_status')


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
            'bring_blurb': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'bring_skillsets_json': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'can_start': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'event': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['profiles.Event']", 'null': 'True', 'blank': 'True'}),
            'event_status': ('django.db.models.fields.CharField', [], {'default': "'Pending'", 'max_length': '25'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'idea_status': ('django.db.models.fields.CharField', [], {'max_length': '25', 'null': 'True', 'blank': 'True'}),
            'mugshot': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'need_skillsets_json': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'past_experience_blurb': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'privacy': ('django.db.models.fields.CharField', [], {'default': "'registered'", 'max_length': '15'}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'related_name': "'profile'", 'unique': 'True', 'to': "orm['auth.User']"})
        },
        'profiles.linkedinprofile': {
            'Meta': {'object_name': 'LinkedinProfile'},
            'fd_profile': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['profiles.FdProfile']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'oauth_object': ('django.db.models.fields.TextField', [], {'max_length': '500'}),
            'profile_industry': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'profile_location': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'profile_picture': ('django.db.models.fields.URLField', [], {'max_length': '200', 'null': 'True', 'blank': 'True'}),
            'profile_raw': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['profiles']
