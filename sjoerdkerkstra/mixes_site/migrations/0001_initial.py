# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Mixclouditem'
        db.create_table(u'mixes_site_mixclouditem', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('description', self.gf('django.db.models.fields.CharField')(default='', max_length=1024, blank=True)),
        ))
        db.send_create_signal(u'mixes_site', ['Mixclouditem'])


    def backwards(self, orm):
        # Deleting model 'Mixclouditem'
        db.delete_table(u'mixes_site_mixclouditem')


    models = {
        u'mixes_site.mixclouditem': {
            'Meta': {'object_name': 'Mixclouditem'},
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['mixes_site']