# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Mixclouditem.description'
        db.alter_column(u'mixes_site_mixclouditem', 'description', self.gf('django.db.models.fields.TextField')(max_length=1024))

    def backwards(self, orm):

        # Changing field 'Mixclouditem.description'
        db.alter_column(u'mixes_site_mixclouditem', 'description', self.gf('django.db.models.fields.CharField')(max_length=1024))

    models = {
        u'mixes_site.mixclouditem': {
            'Meta': {'object_name': 'Mixclouditem'},
            'description': ('django.db.models.fields.TextField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mix_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'user_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'})
        }
    }

    complete_apps = ['mixes_site']