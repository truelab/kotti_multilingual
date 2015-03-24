Changelog
=========

0.2.2truelab (unreleased)
-------------------------

- Deprecated ``api.update_schema`` (use ``widget.i10n_widget_factory`` instead).

- Added ``widget.i10n_widget_factory`` deferred widget.
  Turns field into readonly mode if the context is a translation.
  Obviously this widget makes sense only on edit forms.

  If you area going to apply the i10n_widget_factory for a required field, you'll
  have to provide a deferred missing function


0.2.1truelab (2015-03-12)
-------------------------

- Added a ``kotti_multilingual.blacklist`` setting with a list of type names
  not translatable

- Changed policy for translate action. Now the translated document is automatically
  filled with the parent translation (enhanced usability since we don't have the screen
  splitted in two parts like LinguaPlone). This is possible thanks to a change in 
  sqla.py since we don't set language independent attributes on translated documents

0.2truelabdev (2015-03-11)
--------------------------

- Maintain translation links between content items, with translation source
  and targets.

- Add a translation dropdown UI for adding a translation of an item.

- Fixed translation of objects with not nullable fields

- Added support for sqlalchemy's association_proxy

- Fixed intermittent problem with get_source (integrity error)

- Added ``api.update_schema`` that turns language independent nodes widgets
  into readonly mode 

0.1a3 - 2013-05-08
------------------

- Rename ``LanguageSection`` to ``LanguageRoot`` to better fit Kotti's
  ``INavigationRoot``.  This implies a change in the DB schema for which no
  automatic schema migration is available; you'll have to rename the table
  ``language_sections`` to ``language_roots`` yourself.

- Add some tests.

0.1a2 - 2013-05-07
------------------

- Removed a lot of code that's now replaced by Kotti's ``INavigationRoot`` /
  ``TemplateAPI.navigation_root``.  This greatly simplifies the setup of
  ``kotti_multilingua``.

- Depend on Kotti>=0.9a3dev (needed for the above).

0.1a1 - 2013-05-06
------------------

- Initial release.
