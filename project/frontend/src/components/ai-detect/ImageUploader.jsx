import { useCallback, useRef, useState } from 'react'

const ACCEPTED_TYPES = ['image/jpeg', 'image/png', 'image/jpg', 'image/webp']

export default function ImageUploader({ onFileSelected, previewUrl, onRemove }) {
  const [isDragging, setIsDragging] = useState(false)
  const inputRef = useRef(null)

  const handleFiles = useCallback(
    (files) => {
      const file = files?.[0]
      if (!file) return
      if (!ACCEPTED_TYPES.includes(file.type)) {
        alert('Please upload a JPEG, PNG, or WEBP image.')
        return
      }
      onFileSelected(file)
    },
    [onFileSelected]
  )

  function handleDrop(e) {
    e.preventDefault()
    setIsDragging(false)
    handleFiles(e.dataTransfer.files)
  }

  if (previewUrl) {
    return (
      <div className="uploader__preview">
        <img src={previewUrl} alt="Selected crop leaf" />
        <button type="button" className="btn btn--secondary" onClick={onRemove}>
          ✕ Remove Image
        </button>
      </div>
    )
  }

  return (
    <div
      className={`uploader__dropzone ${isDragging ? 'uploader__dropzone--active' : ''}`}
      onDragOver={(e) => {
        e.preventDefault()
        setIsDragging(true)
      }}
      onDragLeave={() => setIsDragging(false)}
      onDrop={handleDrop}
      onClick={() => inputRef.current?.click()}
      role="button"
      tabIndex={0}
    >
      <p className="uploader__icon">📷</p>
      <p>Drag & drop a crop leaf image here</p>
      <p className="uploader__or">or</p>
      <button type="button" className="btn btn--primary">
        Browse Image
      </button>
      <input
        ref={inputRef}
        type="file"
        accept={ACCEPTED_TYPES.join(',')}
        hidden
        onChange={(e) => handleFiles(e.target.files)}
      />
    </div>
  )
}
