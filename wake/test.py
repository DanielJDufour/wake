from os.path import abspath, dirname, join
from unittest import TestCase
import wake

path_to_data = join(dirname(abspath(__file__)), "data")

class WikidataEntityStreaming(TestCase):
  def test_get_wikidata_entities(self):
    print("starting test_get_wikidata_entities")
    entity_ids = set()
    for index, entity in enumerate(wake.get_wikidata_entities()):
      entity_ids.add(entity['id'])
      if index == 4:
        break
    self.assertEqual(len(entity_ids), 5)
  def test_get_instances_of(self):
    print("starting test_get_instances_of")
    count = 0
    for entity in wake.get_wikidata_entities(instance_of="Q5"):
      count += 1
      print("found human")
      instances = entity['claims']['P31']
      memberships = set("Q" + str(wake.safeget(i, "mainsnak", "datavalue", "value", "numeric-id")) for i in instances)
      self.assertTrue('Q5' in memberships)
      if count >= 5:
        break

class TestMethods(TestCase):
  
  def test_get_nested_links(self):
    text = """ish fleet defeated Alfred's fleet, which may have been weakened in the previous engagement.{{sfn|Woodruff|1993|p=86}}
[[File:Southwark Bridge City Plaque.JPG|thumb|A plaque in the [[City of London]] noting the restoration of the Roman walled city by Alfred.]]
A year later, in 886, Alfre"""
    links = wake.get_links(text)
    self.assertEqual(len(links), 2)
    
    text = """They landed in [[Toulon]] with only Napoleon's pay for their support.
[[File:2016 Napoleon Totenmaske.jpg|thumb|left|[[Death mask]] [[Napoleon Bonaparte|Napoleon]]]]
The Bonapartes moved to [[Marseille]] but in August Toulon offered itself to the British and received the protection of a fleet under [[Samuel Hood, 1st Viscount Hood|Admiral Hood]]."""
    links = wake.get_links(text)
    self.assertEqual(len(links), 6)
    
    filepath = join(path_to_data, "Ajaccio.txt")
    with open(filepath, "r") as f:
      text = f.read()
    links = wake.get_links(text)
    self.assertEqual(len(links), 295)
    
    
  def test_find_index_of_sublist(self):
    types = ["open", "open", "close", "close"]
    open_index, close_index = wake.find_index_of_sublist(types, ["open", "close"])
    self.assertEqual(open_index, 1)
    self.assertEqual(close_index, 2)

    types = ["open", "open", "close", "close", "open", "close"]
    open_index, close_index = wake.find_index_of_sublist(types, ["open", "close"])
    self.assertEqual(open_index, 1)
    self.assertEqual(close_index, 2)

  def test_remove_references(self):
    text = '""<ref name=""EB1910""/>'
    cleaned = wake.remove_references(text)
    self.assertEqual(cleaned, '""')