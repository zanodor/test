/* in Edit mode */

.cm-quote {
    color: var(--text-normal) !important;
  }
  
div:not(.CodeMirror-activeline)>.CodeMirror-line span.cm-formatting-quote {
  color: transparent !important;
  display: inline !important;
}  
  
div:not(.CodeMirror-activeline)>.HyperMD-quote {
  border-left: 4px solid var(--text-selection);
  border-color: var(--text-accent);
  border-top-right-radius: 5px;
  border-bottom-right-radius: 5px;
  border-top-left-radius: 3px;
  border-bottom-left-radius: 3px;
  line-height: 1.3em;
  padding: 12px 0px 15px 8.5px; /* or 12px 15px 15px 8.5px ? */
  margin-right: 15px !important;
  margin-left: 15px !important; /* or 5px ? */
  border-top: transparent;
  border-bottom: transparent;
  background: linear-gradient(120deg, var(--background-secondary), var(--text-faint));
  display: inline-block;
}
  
div:not(.CodeMirror-activeline)>.HyperMD-quote::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0px;
  height: 2px;
  width: 60%;
  background: linear-gradient(90deg, var(--text-accent), var(--text-faint));
}
  
div:not(.CodeMirror-activeline)>.HyperMD-quote::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0px;
  height: 2px;
  width: 25%;
  background: linear-gradient(90deg, var(--text-accent), var(--text-faint));
}
/* in Preview mode */

.markdown-preview-view blockquote {
  position: relative;
  padding: 1rem 2rem 1rem 3rem;
  color: white; /* #bdbdbd */
  line-height: 1.4em;
  border-top-right-radius: 5px;
  border-bottom-right-radius: 5px;
  border-top-left-radius: 3px;
  border-bottom-left-radius: 3px;
  margin-bottom: 2em;
  border-left: 4px rgba(31, 178, 129, 0.9) solid;
  border-top: transparent;
  border-bottom: transparent;
  background: linear-gradient(135deg, var(--base4), var(--base3));
  border-right: transparent;
  display: inline-block;
  margin-right: 0 !important;
}

.markdown-preview-view blockquote::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0px;
  height: 2px;
  width: 60%;
  background: linear-gradient(90deg, rgba(31, 178, 129, 0.9), var(--base3));
}

.markdown-preview-view blockquote::after {
  content: '';
  position: absolute;
  bottom: 0;
  left: 0px;
  height: 2px;
  width: 25%;
  background: linear-gradient(90deg, rgba(31, 178, 129, 0.9), var(--base3));
}

.markdown-preview-view blockquote p {
  position: relative;
}