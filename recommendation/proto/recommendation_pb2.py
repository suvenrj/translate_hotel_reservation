# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: recommendation.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x14recommendation.proto\x12\x0erecommendation\"4\n\x07Request\x12\x0f\n\x07require\x18\x01 \x01(\t\x12\x0b\n\x03lat\x18\x02 \x01(\x01\x12\x0b\n\x03lon\x18\x03 \x01(\x01\"\x1a\n\x06Result\x12\x10\n\x08HotelIds\x18\x01 \x03(\t2W\n\x0eRecommendation\x12\x45\n\x12GetRecommendations\x12\x17.recommendation.Request\x1a\x16.recommendation.Resultb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'recommendation_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _REQUEST._serialized_start=40
  _REQUEST._serialized_end=92
  _RESULT._serialized_start=94
  _RESULT._serialized_end=120
  _RECOMMENDATION._serialized_start=122
  _RECOMMENDATION._serialized_end=209
# @@protoc_insertion_point(module_scope)