# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Mixclouditem.user_name'
        db.add_column(u'mixes_site_mixclouditem', 'user_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)

        # Adding field 'Mixclouditem.mix_name'
        db.add_column(u'mixes_site_mixclouditem', 'mix_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=200),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Mixclouditem.user_name'
        db.delete_column(u'mixes_site_mixclouditem', 'user_name')

        # Deleting field 'Mixclouditem.mix_name'
        db.delete_column(u'mixes_site_mixclouditem', 'mix_name')


    models = {
        u'mixes_site.mixclouditem': {
            'Meta': {'object_name': 'Mixclouditem'},
            'description': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '1024', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mix_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'}),
            'user_name': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '200'})
        }
    }

    complete_apps = ['mixes_site']